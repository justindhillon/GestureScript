// How large memory blocks are (size of array)
const MEMORY_SIZE = 10000;

const TOKEN_PLUS = '1';
const TOKEN_MINUS = '2';
const TOKEN_PREVIOUS = '3';
const TOKEN_NEXT = '4';
const TOKEN_LOOP_START = '5';
const TOKEN_LOOP_END = '6';
const TOKEN_OUTPUT = '7';

// 1, 2 is ✋ ✋-left
// 3, 4 is 👈 👈-left
// 5, 6 is 🤟 🤟-left
// 7 is 👌

// Hello World!
// 1111111154111154114111411141333326414142441536326447422271111111771117447327371117222222722222222744174117

export function interpreter(signs: string): string | null {
    const memory = new Array(MEMORY_SIZE).fill(0);
    let signPointer: number = 0;
    let memoryPointer: number = 0;
    let addressStack: number[] = [];

    let output: string = "";
    let terminate: boolean = false;

    while (!terminate) {
        switch (signs[signPointer]) {
            case TOKEN_PLUS:
                memory[memoryPointer]++;
                break;
            case TOKEN_MINUS:
                memory[memoryPointer]--;
                break;
            case TOKEN_PREVIOUS:
                if (0 < memoryPointer)
                    memoryPointer--;
                break;
            case TOKEN_NEXT:
                if (memoryPointer === memory.length - 1) 
                    // Out of memory, allocate another block
                    memory.push(new Array(MEMORY_SIZE).fill(0));
                memoryPointer++;
                break;
            case TOKEN_LOOP_START:
                if (memory[memoryPointer]) {
                    addressStack.push(signPointer);
                } else {
                    // Goto TOKEN_LOOP_END
                    let nestedLoops = 0;
                    while (true) {
                        signPointer++;
                        if (!signs[signPointer]) 
                            // The program has been executed
                            break;
                        if (signs[signPointer] === TOKEN_LOOP_START) {
                            nestedLoops++;
                        } else if (signs[signPointer] === TOKEN_LOOP_END) {
                            if (nestedLoops) {
                                nestedLoops--;
                            } else {
                                break;
                            }
                        }
                    }
                }
                break;
            case TOKEN_LOOP_END:
                signPointer = (addressStack.pop() ?? 0) - 1;
                break;
            case TOKEN_OUTPUT:
                output += String.fromCharCode(memory[memoryPointer]);
                break;
            case undefined:
                // The program has been executed
                terminate = true;
                break;
            default:
                console.error("Error: signs includes invalid value", signs[signPointer]);
                return null;
        }
        signPointer++; 
    }

    return output;
}
