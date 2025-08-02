pipeline {

    agent any 

    stages {

        stage("build") {

            steps {
                echo "Building stage"
                sh "apt install tree -y"
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
                sh "tree"
            }
        }
    }
}