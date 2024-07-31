pipeline {
  agent any
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  environment {
    DOCKERHUB_CREDENTIALS = credentials('angelocapone')
  }
  stages {
    stage('Build') {
      steps {
        bat 'docker rmi angelocapone/modelonweb --force'
		    bat 'docker build -t angelocapone/modelonweb:v2 .'
      }
    }
    stage('Login') {
      steps {
        bat 'echo %DOCKERHUB_CREDENTIALS_PSW% | docker login -u %DOCKERHUB_CREDENTIALS_USR% --password-stdin'
      }
    }
    stage('Push') {
      steps {
        bat 'docker push angelocapone/modelonweb:v2'
      }
    }
  }
  post {
    always {
      bat 'docker logout'
    }
  }
}