/*
Notes: Need Python 3.11 for utils test. >=3.9 is fine for ai test. Need nodejs jenkins plugin for react build step
*/

pipeline {
    agent any

    environment {
        OPENAI_API_KEY='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'
    }

    //install nodejs plugin, go to manage jenkins->tools->nodejs
    tools { nodejs "nodejs" }

    stages {
        
        stage('Checkout') {
            steps {
                script {
                    git branch: "master",
                    credentialsId: 'bitbucket',
                    url: 'https://bitbucket.cantaloupe.com:8443/scm/us/ai-assistant.git'
                }
            }
        }
        
        stage('Install Dependencies & Test') {
            steps {
                script {
                    //Generate requirements.txt and install dependencies
                    
                    dir('ai') {
                        //python -m venv ai_test
                        //source ai_test/bin/activate
                        //pip install --upgrade pip
                        //pip install pipenv
                        //pipenv requirements > requirements.txt
                        //pip install -r requirements.txt
                        //pytest
                        sh '''
                            python3.11 -m pip install --upgrade pip
                            python3.11 -m pip install pipenv
                            python3.11 -m pipenv --python 3.11
                            python3.11 -m pipenv install --ignore-pipfile
                            python3.11 -m pipenv run pytest
                        '''
                    }
                    
                    dir('utils') {
                        /*
                        python3 -m venv utils_test
                        source utils_test/bin/activate
                        pip install --upgrade pip
                        pip install pipenv
                        pipenv requirements > requirements.txt
                        pip install -r requirements.txt
                        pytest
                        */
                        sh '''
                            python3.11 -m pip install --upgrade pip
                            python3.11 -m pip install pipenv
                            python3.11 -m pipenv --python 3.11
                            python3.11 -m pipenv install --ignore-pipfile
                            python3.11 -m pipenv install exceptiongroup
                            python3.11 -m pipenv run pytest
                        '''
                    }
                }
            }
        }
        
        stage('Build React') {
            steps {
                script {
                    dir('client') {
                        sh '''
                            npm install
                            npm run build
                        '''
                    }
                }
            }
        }
        /*
        stage('Deploy') {
            steps {
                //
            }
        }
        */
    }
}