from subprocess import Popen, PIPE
from app.utils import LOG

class ConfigsCommand():
    def __init__(self):
        pass

    def _exec_cmd(self, cmd):
        cmd = '/root/kafka/bin/kafka-configs.sh {cmd}'.format(cmd = cmd)
        LOG.info('[Command] {cmd}'.format(cmd = cmd))
        p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        stdout, stderr =  p.communicate()
        if p.returncode != 0:
            LOG.error('[kafka-configs] failed')
            LOG.error('[kafka-configs] {stderr}'.format(stderr = stderr))
            LOG.error('[kafka-configs] {stdout}'.format(stdout = stdout))
        return (p.returncode, stdout)

    def create_user(self, username, password):
        pwd = "'SCRAM-SHA-256=[password={password}],SCRAM-SHA-512=[password={password}]'".format(password = password) 
        cmd = "--zookeeper localhost:2181 --alter --add-config {pwd} --entity-type users --entity-name {username}".format(pwd = pwd, username = username)
        _, stdout = self._exec_cmd(cmd)
        LOG.info('[create_user] {stdout}'.format(stdout = stdout))
        return stdout

    def get_user(self, username):
        cmd = '--zookeeper localhost:2181 --describe --entity-type users --entity-name {username}'.format(username = username)
        _, stdout = self._exec_cmd(cmd)
        LOG.info('[get_user] {stdout}'.format(stdout = stdout))
        return stdout
    
    def list_user(self):
        cmd = '--zookeeper localhost:2181 --describe --entity-type users'
        _, stdout = self._exec_cmd(cmd)
        LOG.info('[list_user] {stdout}'.format(stdout = stdout))
        return stdout
    
    def delete_user(self):
        pass

    def update_user(self):
        pass

class TopicsCommand():
    def __init__(self):
        pass
    
    def _exec_cmd(self, cmd):
        cmd = '/root/kafka/bin/kafka-topics.sh {cmd}'.format(cmd = cmd)
        LOG.info('[Command] {cmd}'.format(cmd = cmd))
        p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        stdout, stderr =  p.communicate()
        if p.returncode != 0:
            LOG.error('[kafka-topics] failed')
            LOG.error('[kafka-topics] {stdout}'.format(stdout = stdout))
            LOG.error('[kafka-topics] {stderr}'.format(stderr = stderr))
        return (p.returncode, stdout)

    def create_topic(self, topic_name, replication_factor, partitions):
        cmd = '/root/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor {replication_factor} --partitions {partitions} --topic {topic_name}'.format(topic_name = topic_name, replication_factor = replication_factor, partitions = partitions)
        _, stdout = self._exec_cmd(cmd)
        LOG.info('[create_topic] {stdout}'.format(stdout = stdout))
        return stdout

    def list_topic(self):
        cmd = '/root/kafka/bin/kafka-topics.sh --list --zookeeper localhost:2181'
        _, stdout = self._exec_cmd(cmd)
        LOG.info('[list_topic] {stdout}'.format(stdout = stdout))
        return stdout

class AclsCommand():
    def __init__(self):
        pass

    def _exec_cmd(self, cmd):
        cmd = '/root/kafka/bin/kafka-acls.sh {cmd}'.format(cmd = cmd)
        p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        stdout, stderr =  p.communicate()
        if p.returncode != 0:
            LOG.error('[kafka-acls] failed')
            LOG.error('[kafka-acls] {stdout}'.format(stdout = stdout))
            LOG.error('[kafka-acls] {stderr}'.format(stderr = stderr))
        return (p.returncode, stdout)

    def create_producer_acl(self, username, topic):
        user = 'User:{username}'.format(username = username)
        cmd = '--authorizer-properties zookeeper.connect=localhost:2181 --add --allow-principal {user} --producer --topic {topic}'.format(user = user, topic = topic)
        _, stdout = self._exec_cmd(cmd)
        LOG.info('[create_producer_acl] {stdout}'.format(stdout = stdout))
        return stdout

    def create_consumer_acl(self, username, topic):
        user = 'User:{username}'.format(username = username)
        cmd = '--authorizer-properties zookeeper.connect=localhost:2181 --add --allow-principal {user} --consumer --group=* --topic {topic}'.format(user = user, topic = topic)
        _, stdout = self._exec_cmd(cmd)
        LOG.info('[create_consumer_acl] {stdout}'.format(stdout = stdout))
        return stdout