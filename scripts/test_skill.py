#!/usr/bin/env python3
import asyncio
import os
import sys

# Add project root to path if needed
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google.antigravity import Agent, LocalAgentConfig

async def test_generation():
    print("🧪 Running local System Design Educator skill integration test...")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    skills_path = os.path.join(project_root, "skills")
    output_file = os.path.join(project_root, "Questions_and_Answers", "URL_Shortner", "URL_Shortner.md")

    # 1. Clean previous run
    if os.path.exists(output_file):
        print("🧹 Cleaning up old test output...")
        os.remove(output_file)

    # 2. Invoke local Agent with the skill
    config = LocalAgentConfig(
        skills_paths=[skills_path]
    )

    prompt = (
        "You have the 'system-design-educator' skill. "
        "Please generate a premium, interview-ready system design case study for a 'URL Shortener' in Markdown. "
        "Strictly adhere to the simulated interviewer Q&A dialogue, estimations, database schemas, "
        "and customized HSL Mermaid architectures. Output ONLY the raw markdown content without enclosing code blocks."
    )

    try:
        print("🤖 Invoking AGY agent to generate URL Shortener design case study...")
        async with Agent(config=config) as agent:
            response = await agent.chat(prompt)
            content = await response.text()

        # 3. Save output
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"💾 Saved generated case study to: {output_file}")

        # 4. Automated verification tests
        print("\n🔍 Verifying generated structure & requirements...")
        
        errors = []
        
        # Check file length
        if len(content) < 1000:
            errors.append("❌ Output file is too short (less than 1000 characters).")

        # Check for simulated dialogue section
        if "dialogue" not in content.lower() and "questions" not in content.lower() and "candidate" not in content.lower():
            errors.append("❌ Missing simulated Candidate/Interviewer clarifying questions dialogue.")

        # Check for Mermaid diagram
        if "mermaid" not in content.lower():
            errors.append("❌ Missing Mermaid architectural diagram.")

        # Check for API specifications
        if "api" not in content.lower() and "endpoints" not in content.lower():
            errors.append("❌ Missing API Design section.")

        # Check for database schema details
        if "schema" not in content.lower() and "database" not in content.lower() and "table" not in content.lower():
            errors.append("❌ Missing Database Schema or Storage models.")

        # Check for scale math
        if "estimation" not in content.lower() and "qps" not in content.lower() and "tb" not in content.lower():
            errors.append("❌ Missing Back-of-the-envelope calculations.")

        if errors:
            print("\n❌ Test Failed! Structural issues found:")
            for err in errors:
                print(err)
            sys.exit(1)
        else:
            print("\n✅ Test Passed! The system design learning module was generated with premium structure and aesthetics.")
            sys.exit(0)

    except Exception as e:
        print(f"❌ Test Failed due to SDK or communication error: {e}")
        print("Please make sure GEMINI_API_KEY is configured correctly.")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(test_generation())
