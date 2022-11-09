pipeline {
	agent none
	stages {
		stage('Build') {
			agent {
				docker 'python-gcloud'
				
				steps {
					sh 'pytest /scr'
				}
			}
		}
	}
}