pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                pip install requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd src
                flask run
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}