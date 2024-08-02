pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        bat 'docker build -t angelocapone/modelonweb:v2 .'
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
      cleanWs() // Pulisce la workspace
    }
  }
}