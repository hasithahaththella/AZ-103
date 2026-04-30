# Prerequisists : 
# Install : pip install azure-ai-projects azure-identity openai

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient, ProjectsClient

project_endpoint = "https://{resource-name}.services.ai.azure.com/api/projects/<project-name>"

# provides access to Foundry-native operations that don't have OpenAI equivalents.
project_client = AIProjectClient(
    endpoint = project_endpoint, 
    credential = DefaultAzureCredential()) 

# create a chat client
openapi_client = project_client.get_openai_client(api_version="2024-10-01")