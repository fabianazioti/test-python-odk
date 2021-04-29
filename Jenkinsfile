try {
   timeout(time: 20, unit: 'MINUTES') {
      node('python') {
          stage('build') {
            openshiftBuild(buildConfig: 'jenkins', showBuildLogs: 'true')
          }
          stage('deploy') {
            openshiftDeploy(deploymentConfig: 'jenkins')
          }
        }
   }
} catch (err) {
   echo "in catch block"
   echo "Caught: ${err}"
   currentBuild.result = 'FAILURE'
   throw err
}
