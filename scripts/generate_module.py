#!/usr/bin/env python3
import asyncio
import os
import sys
from google.antigravity import Agent, LocalAgentConfig

async def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate_module.py <topic>")
        print("Example: python3 generate_module.py 'URL Shortener'")
        sys.exit(1)

    topic = sys.argv[1]
    print(f"🚀 Generating system design learning module for: '{topic}' using google-antigravity...")

    # Ensure API Key is present
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("⚠️ Warning: GEMINI_API_KEY environment variable is not set.")
        print("Please obtain an API key from: https://aistudio.google.com/app/api-keys")
        print("Proceeding using default environment credentials if configured...")

    # Absolute path to the skill folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    skills_path = os.path.join(project_root, "skills")

    print(f"📂 Loading skill from: {skills_path}")

    # Set up config with skills_paths
    config = LocalAgentConfig(
        skills_paths=[skills_path]
    )

    prompt = (
        f"You have the 'system-design-educator' skill. "
        f"Please write a comprehensive, visually stunning, interview-ready system design learning module "
        f"for the topic '{topic}' in Markdown format. "
        f"Ensure it strictly adheres to all structure and styling requirements outlined in the skill's instructions. "
        f"Generate ONLY the raw Markdown content for the module, without enclosing it in markdown blocks or markdown syntax."
    )

    try:
        async with Agent(config=config) as agent:
            # Send standard chat to the agent to generate content
            print("🤖 Calling AGY agent chat...")
            response = await agent.chat(prompt)
            content = await response.text()
            
            # Format folder and filename dynamically as Questions_and_Answers/Topic_Name/Topic_Name.md
            folder_name = topic.replace(" ", "_")
            output_path = os.path.join(project_root, "Questions_and_Answers", folder_name, f"{folder_name}.md")

            # Ensure basics dir exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            print(f"💾 Saving generated content to: {output_path}")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)
            
            print(f"✨ Module '{topic}' generated successfully!")

    except Exception as e:
        print(f"❌ Error during module generation: {e}")
        print("\nPlease ensure you have installed the 'google-antigravity' library and have configured your credentials.")

if __name__ == "__main__":
    asyncio.run(main())
