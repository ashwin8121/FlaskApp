pipeline {

    agent any 

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