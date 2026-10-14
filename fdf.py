import os

try:
    from PyPDF2 import PdfMerger
except ImportError:
    try:
        from pypdf import PdfMerger
    except ImportError as exc:
        raise ImportError(
            "Neither 'PyPDF2' nor 'pypdf' is installed. Install one of them with: "
            "pip install PyPDF2 or pip install pypdf"
        ) from exc

def merge_pdfs(pdf_files, output_file):
    merger = PdfMerger()

    try:
        for pdf in pdf_files:
            if os.path.isfile(pdf):
                merger.append(pdf)
                print(f"Added: {pdf}")
            else:
                print(f"File not found: {pdf}")

        merger.write(output_file)
        print(f"\nMerged PDF saved as:\n{output_file}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        merger.close()


pdf_files = [
    r"C:\Users\adity\Downloads\New folder\Linux_Notes_Session1.pdf",
    r"C:\Users\adity\Downloads\New folder\Session2 Notes.pdf",
    r"C:\Users\adity\Downloads\New folder\Session-3-Shell-Scripting-Notes.pdf",
    r"C:\Users\adity\Downloads\New folder\Session4-Student-Notes.pdf",
    r"C:\Users\adity\Downloads\New folder\Session6-AWS-Student-Notes.pdf",
    r"C:\Users\adity\Downloads\New folder\Session7-AWS-Student-Notes.pdf",
    r"C:\Users\adity\Downloads\New folder\Session8-Serverless-Student-Notes.pdf",
    r"C:\Users\adity\Downloads\New folder\Session9-Git-Student-Notes.pdf",
    r"C:\Users\adity\Downloads\New folder\Session10-Advanced-Git-Student-Notes.pdf",
    r"C:\Users\adity\Downloads\New folder\Session11-Networking-Student-Notes.pdf",
    r"C:\Users\adity\Downloads\New folder\Session12-Docker-Student-Notes (1).pdf",
    r"C:\Users\adity\Downloads\New folder\Session13-Docker-Networking-Volumes-Security-Student-Notes.pdf",
    r"C:\Users\adity\Downloads\New folder\Session14-SonarQube-Quality-Gates-Student-Notes.pdf",
    r"C:\Users\adity\Downloads\New folder\Session15-Jenkins-CICD-Student-Notes.pdf",
    r"C:\Users\adity\Downloads\New folder\Session17-Kubernetes-Introduction-Student-Notes (1).pdf",
    r"C:\Users\adity\Downloads\New folder\Session19-Kubernetes-on-AWS-Student-Notes.pdf",
    r"C:\Users\adity\Downloads\New folder\Session21-Ansible-HandsOn-Lab.pdf",
    r"C:\Users\adity\Downloads\New folder\Session21-Getting-Started-with-Ansible-Student-Notes.pdf",
    r"C:\Users\adity\Downloads\New folder\Session22-Automation-with-Ansible-Student-Notes.pdf",
    r"C:\Users\adity\Downloads\New folder\Session23-Terraform-Introduction-Student-Notes.pdf",
    r"C:\Users\adity\Downloads\New folder\Session24-Terraform-Advanced-Monitoring-HandsOn-Lab.pdf",
    r"C:\Users\adity\Downloads\New folder\Session24-Terraform-Advanced-Monitoring-Student-Notes.pdf"
]

output_file = r"C:\Users\adity\Downloads\New folder\merged.pdf"

merge_pdfs(pdf_files, output_file)