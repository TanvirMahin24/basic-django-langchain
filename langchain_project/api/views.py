from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import SystemMessage, HumanMessage
from django.conf import settings

@csrf_exempt
@require_http_methods(["POST"])
def ask(request):
    try:
        data = json.loads(request.body)
        message = data.get('message', '')
        
        if not message:
            return JsonResponse(
                {'error': 'Message is required'}, 
                status=400
            )
        
        # Initialize LangChain with Google Gemini
        llm = ChatGoogleGenerativeAI(
            google_api_key=settings.GOOGLE_API_KEY,
            model="gemini-2.5-flash",
            temperature=0.7
        )
        
        # Define system prompt
        system_prompt = """You are a helpful AI assistant. 
        Provide clear, concise, and accurate responses to user queries."""
        
        # Create chat prompt template
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=message)
        ]
        
        # Get response from LangChain
        response = llm.invoke(messages)
        
        return JsonResponse({
            'response': response.content,
            'message': message
        })
        
    except Exception as e:
        return JsonResponse(
            {'error': str(e)}, 
            status=500
        )