import json

def parse_resume(file_path):
    try:
        # Load JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Basic Info
        print("\n=== BASIC INFO ===")
        print("Name:", data.get("name", ""))
        print("Email:", data.get("email", ""))
        print("Phone:", data.get("phone", ""))
        print("Summary:", data.get("summary", ""))

        # Work Experience
        print("\n=== WORK EXPERIENCE ===")
        for exp in data.get("work_experience", []):
            print("\nCompany:", exp.get("company_name", ""))
            print("Duration:", exp.get("start_date", ""), "-", exp.get("end_date", ""))
            print("Description:", exp.get("description", ""))

        # Education
        print("\n=== EDUCATION ===")
        for edu in data.get("education", []):
            print("\nInstitute:", edu.get("college_or_school_name", ""))
            print("Course:", edu.get("course_name", ""))
            print("Duration:", edu.get("start_date", ""), "-", edu.get("end_date", ""))
            print("Marks:", edu.get("marks", ""))

        # Skills
        print("\n=== SKILLS ===")
        print(", ".join(data.get("skills", [])))

        # Projects
        print("\n=== PROJECTS ===")
        for proj in data.get("projects", []):
            print("\nProject Name:", proj.get("project_name", ""))
            print("Description:", proj.get("description", ""))
            print("Technologies:", ", ".join(proj.get("technologies_used", [])))

        # Certificates
        print("\n=== CERTIFICATES ===")
        for cert in data.get("certificates", []):
            print("\nCourse:", cert.get("course_name", ""))
            print("Institute:", cert.get("institute", ""))
            print("Completion Date:", cert.get("completion_date", ""))

        # Achievements
        print("\n=== ACHIEVEMENTS ===")
        for ach in data.get("achievements", []):
            print("-", ach)

        # Languages
        print("\n=== LANGUAGES ===")
        print(", ".join(data.get("languages", [])))

        # Portfolio Links
        print("\n=== PORTFOLIO LINKS ===")
        for link in data.get("portfolio_links", []):
            print("-", link)

    except FileNotFoundError:
        print("Error: File not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")


# Run parser
if __name__ == "__main__":
    parse_resume("Sample_Output.json")