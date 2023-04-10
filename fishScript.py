import subprocess

# Launch two separate processes to run script1.py and script2.py
process1 = subprocess.Popen(['python', 'nostaleScript.py'])
process2 = subprocess.Popen(['python', 'nostaleScript2.py'])

# Wait for both processes to complete
process1.wait()
process2.wait()