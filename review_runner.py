from ai_engine import ai_review
from jenkins_analyzer import load_past_failures

def main():
    with open("diff.txt", "r") as f:
        diff = f.read()

    if not diff.strip():
        print("No changes found")
        return

    past_logs = str(load_past_failures()[:3])

    print("🚀 AI Review Running...\n")

    result = ai_review(diff, "branch_diff", past_logs)

    print("\n=== AI SUGGESTIONS ===\n")
    print(result)

if __name__ == "__main__":
    main()
