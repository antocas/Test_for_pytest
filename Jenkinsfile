pipeline {
	agent any
	stages {
		stage('Build') {
			agent {
				docker {
					image 'python-gcloud'
				}
				steps {
					sh 'pytest /scr'
				}
			}
		}
	}
}