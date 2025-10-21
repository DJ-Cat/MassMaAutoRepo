# By adding 'src.', we tell Python to look inside the 'src' folder.
# I've also updated the names to match your files: 'profiling' and 'scoring'.
from src.profiling import extract_text_from_pdf, create_profile
from src.scoring import calculate_score

def analyze_applicant(applicant_pdf_path, dorm_pdf_path):
    """
    Main function to run the analysis of an applicant against a dorm description.
    """
    print("--- Starting Analysis ---")

    # --- Step 1: Process Dorm PDF ---
    print(f"\n1. Extracting text from dormitory PDF: {dorm_pdf_path}")
    dorm_text = extract_text_from_pdf(dorm_pdf_path)
    if dorm_text.startswith("Error"):
        print(dorm_text)
        return

    print("2. Creating dormitory profile...")
    dorm_profile = create_profile(dorm_text)
    if dorm_profile is None:
        print("Failed to create dorm profile. Exiting.")
        return
    print("Dormitory Profile Created.")
    # print("Dorm Profile Data:", dorm_profile) # Uncomment to debug

    # --- Step 2: Process Applicant PDF ---
    print(f"\n3. Extracting text from applicant PDF: {applicant_pdf_path}")
    applicant_text = extract_text_from_pdf(applicant_pdf_path)
    if applicant_text.startswith("Error"):
        print(applicant_text)
        return
        
    print("4. Creating applicant profile...")
    applicant_profile = create_profile(applicant_text)
    if applicant_profile is None:
        print("Failed to create applicant profile. Exiting.")
        return
    print("Applicant Profile Created.")
    # print("Applicant Profile Data:", applicant_profile) # Uncomment to debug

    # --- Step 3: Score the Applicant ---
    print("\n5. Calculating compatibility score...")
    score, explanation = calculate_score(applicant_profile, dorm_profile)

    # --- Step 4: Display Results ---
    print("\n--- Analysis Complete ---")
    print(f"Compatibility Score: {score}/100")
    print("\nExplanation:")
    print(explanation)
    print("-------------------------\n")


if __name__ == '__main__':
    # --- IMPORTANT ---
    # Make sure to update these paths to your actual PDF files.
    # Note: I'm using your 'data' folder structure as an example.
    
    applicant_pdf = "/Users/quintenmajica/Desktop/Neuer Ordner/data/input/applicant_profiles/apptext.pdf"

    dormitory_pdf = "/Users/quintenmajica/Desktop/Neuer Ordner/data/input/dorm_descriptions/dormtext.pdf"
    
    analyze_applicant(applicant_pdf, dormitory_pdf)

