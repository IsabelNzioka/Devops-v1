pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code from your version control system (e.g., Git)
                checkout scm
            }
        }

        stage('Test') {
            steps {
                // Install project dependencies (if any)
                sh 'pip install -r requirements.txt'  // If you have a requirements.txt file

                // Run pytest
                sh 'pytest'  // Assumes your tests are in files named test_*.py
            }
        }
    }

    post {
        success {
            // Actions to take when the pipeline succeeds
            echo 'Tests passed successfully.'
        }
        failure {
            // Actions to take when the pipeline fails
            echo 'Tests failed. You can handle failure here.'
        }
    }
}
