pipeline {

    agent  {

        docker {
            
            image 'python:3.10-slim'  // You can change to 3.9, 3.11, etc.
            args '-u root'  // Optional: run as root if needed for installing system packages
        }
    }
    stages {

        stage("build") {

            steps {
                echo "Building stage"
                sh "pip install requirements"
            }
        }
        
        stage("test") {

            steps {
                echo "Testing Stage"
                
            }
        }
        
        stage("deploy") {

            steps {
                echo "Deploying the application"
                sh "python src/app.py"
            }
        }
    }
}