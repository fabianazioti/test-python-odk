pipeline {
    agent none
    stage('build') {
      openshiftBuild(buildConfig: 'test-python-odk', showBuildLogs: 'true')
    }
    stage('deploy') {
      openshiftDeploy(deploymentConfig: 'nodejs-mongodb-example')
    }
}
