pipeline {
    agent any
    stages {
    stage('Build') {
        steps {
            script {
                openshift.withCluster() {
                    openshift.withProject() {
                        openshift.startBuild("test-python-odk").logs('-f')
                    }
                }
            }
        }
    }
    }
}
