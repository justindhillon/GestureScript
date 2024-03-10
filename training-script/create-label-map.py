import subprocess

labels = [
    {'name': '✋',      'id': 1},
    {'name': '✋-left', 'id': 2},
    {'name': '👈',      'id': 3},
    {'name': '👈-left', 'id': 4},
    {'name': '🤟',      'id': 5},
    {'name': '🤟-left', 'id': 6},
    {'name': '👌',      'id': 7}
]

# Create label_map
with open('annotations/label_map.rbtxt', 'w') as file:
    for label in labels:
        file.write('item { \n')
        file.write('\tname:\'{}\'\n'.format(label['name']))
        file.write('\tid:{}\n'.format(label['id']))
        file.write('}\n')

# Create TF records
subprocess.run("python generate_tfrecord.py -x training-images/training -l annotations/label_map.pbtxt -o annotations/train.record", shell=True)
subprocess.run("python generate_tfrecord.py -x training-images/testing  -l annotations/label_map.pbtxt -o annotations/test.record",  shell=True)
