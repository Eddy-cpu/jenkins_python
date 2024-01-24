podTemplate(containers: [
  containerTemplate(
    name: 'python', 
    image: 'jenkins/inbound-agent-python:latest', 
    command: 'sleep',
    args: '30d')
]) 
{
  node(POD_LABEL)
  {
    stage('Get a Python Project')
    {
      container('python')
      {
          stage('Checkout Code')
          {
            sh 'apt update'
            sh 'apt install -y nano'
            echo 'Y'
            sh 'apt install -y pip'
            echo 'Y'
            sh 'apt install python3'
            sh 'pwd'
            sh 'ls -la'
            sh 'python3 -V'
            sh 'hostname'
            sh 'git clone https://github.com/hanley/jenkins_python.git'
            sh 'ls -la jenkins_python'
            sh 'python3 jenkins_python/cal.py'
          }
          stage(' Installing packages')
          {
            sh 'pwd'
            sh 'ls -la'
            sh 'python3 -V'
            sh 'apt-get update && apt-get install -y python3-pip'
            sh 'apt-get install -y python3-venv'
            sh 'echo "Y" | python3 -m venv venv'
            sh '. venv/bin/activate'
            sh 'pip install python3-requests'
            sh 'pip install --user pipx'
            sh 'pipx install python3-requests'
            sh 'python3 jenkins_python/cal.py'
          }
          stage('Static Code Check')
          {
            sh 'pwd'
            sh 'ls -la'
            sh 'python3 -V'
            sh 'ls -la jenkins_python'
            sh 'python3 jenkins_python/cal.py'
          }
          stage('Unit Test Check')
          {
            sh 'python3 jenkins_python/testcal.py'          
          }
        
      }
    }
  }
}
