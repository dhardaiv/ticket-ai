from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

category_prompt = ChatPromptTemplate.from_template("""
You are a ticket classification assistant.
Given the description of a support ticket, assign it to one category:
- IT Cloud Operations
- IT Enterprise Application Services
- IT End User Compute
- IT Level 2 Service Desk
- IT Information Security
- IT Infrastructure Operations
- IT Networks, Security Operations, Telecom
- IT Web Application Support

Ticket:
"{ticket}"

Return ONLY the category name.
""")

category_chain = LLMChain(llm=llm, prompt=category_prompt)

def classify_ticket(ticket: str) -> str:
    return category_chain.run(ticket=ticket).strip()
