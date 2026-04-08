import asyncio
import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY").strip()

llm = ChatOpenAI(
    model="minimax/minimax-m2.5:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    temperature=0.7,
)


async def main():
    server_params = StdioServerParameters(
        command="python3",
        args=["server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            tools = await load_mcp_tools(session)

            # Core function: create LLM agent with MCP tools
            agent = create_agent(
                llm,
                tools,
                system_prompt="""
                You are a smart note-taking assistant.
                Use tools to save, read, search, and delete notes.
                """
            )

            print("✅ Smart Notepad Agent Ready!")
            print("Type 'exit' to quit\n")

            while True:
                user_input = input("You: ")

                if user_input.lower() == "exit":
                    print("Goodbye!!!")
                    break

                # Core function: Python-controlled delete confirmation flow
                if "delete" in user_input.lower():
                    search_response = await agent.ainvoke(
                        {
                            "messages": [
                                {
                                    "role": "user",
                                    "content": (
                                        f"Search the note related to: "
                                        f"{user_input}"
                                    )
                                }
                            ]
                        }
                    )

                    note_result = search_response["messages"][-1].content

                    if "NOT_FOUND" in note_result:
                        print("No matching note found.\n")
                        continue

                    print(f"Found this note:\n{note_result}")

                    confirm = input(
                        "Is this the note you want to delete? (y/n): "
                    )

                    if confirm.lower() == "y":
                        matched_notes = json.loads(note_result)
                        note_title = matched_notes[0]["title"]

                        delete_response = await agent.ainvoke(
                            {
                                "messages": [
                                    {
                                        "role": "user",
                                        "content": (
                                            f"Delete note titled "
                                            f"{note_title}"
                                        )
                                    }
                                ]
                            }
                        )

                        print(
                            f"Answer: "
                            f"{delete_response['messages'][-1].content}\n"
                        )

                    else:
                        print("Deletion cancelled.\n")

                    continue

                # Core function: normal chat + tool usage flow
                response = await agent.ainvoke(
                    {
                        "messages": [
                            {
                                "role": "user",
                                "content": user_input
                            }
                        ]
                    }
                )

                print(f"Answer: {response['messages'][-1].content}\n")


if __name__ == "__main__":
    asyncio.run(main())