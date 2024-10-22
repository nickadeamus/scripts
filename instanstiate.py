from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

@app.route('launch',methods=['POST'])
def launch_instance():
    template_id = request.json.get('template_id')
    version = request.json.get('version','$Latest')

    ec2 = boto3.client('ec2')
    try:
        response = ec2.run_instances(
                LaunchTemplate={
                    'LaunchTemplateId': template_id
                    'Version': version
                    },
                MinCount=1,
                MacCount=1
                )

        instance_id = response['Instances'][0]['InstanceId']
        return jsonify({'status': 'success', 'instance_id': instance_id}), 200
    except Exception as e:
        retrun jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 
