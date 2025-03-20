pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        bat 'docker build -t bncrm/model:v1 .'
      }
    }

    stage('Push') {
      steps {
        bat 'docker push bncrm/model:v1'
      }
    }
  }
  post {
    always {
      cleanWs() // Pulisce la workspace
    }
  }
}
