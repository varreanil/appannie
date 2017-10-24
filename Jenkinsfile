#!/usr/bin/env groovy

node {
  stage('SCM') {
    git 'https://github.com/varreanil/appannie.git'
  }
  stage('Unit Test') {
    sh 'python3 -m unittest discover -s tests'
  }
  stage('Test Coverage') {
    sh 'coverage run --source=. -m unittest discover -s tests'
    sh 'coverage xml -i'
  }
  stage('SonarQube analysis') {
    echo "Anil::: $WORKSPACE"
    sh "ls $WORKSPACE/apiutils"

    // requires SonarQube Scanner 2.8+
    def scannerHome = tool 'sqscanner';
    withSonarQubeEnv('SonarQube-local') {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}