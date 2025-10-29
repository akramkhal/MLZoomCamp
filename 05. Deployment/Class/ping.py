

from flask import Flask

app = Flask('ping')

# In a simple sample implementation, we want to create a ping-pong service. This means we send a “ping” request to a web service, and it responds with “pong.” To achieve this, we create a file named ping.py with the content of the next snippet:

# Add decorator to a function (decorator adds extra functionality).  ‘route’ specifies the address at which the function will be accessible. 
# The ‘method’ specifies how we can access this address. In this case, we want to access the function using the GET method, and it will be located at the ‘/ping’ address.  
@app.route('/ping', methods=['GET'])
def ping():
    return "PONG"

#  block (if __name__ == '__main__') to ensure it is executed only when we run the script using “python ping.py” in the top-level script environment
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)