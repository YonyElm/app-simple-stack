import os


class CloudMetadata:

    def __init__(self):
        self.region = None
        self.instance_id = None

    def getAWSRegion(self):
        return os.popen("curl -s -m 1 http://169.254.169.254/latest/meta-data/placement/region").read()

    def getAWSInstanceId(self):
        return os.popen("curl -s -m 1 http://169.254.169.254/latest/meta-data/instance-id").read()

    def getCloudMetadata(self):
        region = self.getAWSRegion()
        instance = self.getAWSInstanceId()
        if (region==""):
            return {"region": "NONE", "instance_id": "NONE"}
        else:
            return {"region": region, "instance_id": instance}
