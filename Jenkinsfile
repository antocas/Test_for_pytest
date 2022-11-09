pipeline {
    agent none
    stages {
        stage('Test') {
            agent {
                docker {
                    image 'python-gcloud'
                }
            }
            steps {
                sh 'pytest'
            }
        }
    }
}