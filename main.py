from playwright.sync_api import sync_playwright

def fetch_and_save_pdf(url, output_pdf):
    with sync_playwright() as p:
        # Launch the browser in headless mode
        browser = p.chromium.launch(headless=True)
        # Create a new page (tab)
        page = browser.new_page()

        # Navigate to the URL and wait for the network to be idle
        page.goto(url, wait_until='networkidle')  # Ensures all network resources have loaded

        # Add CSS to ensure everything fits within the page and no text or content overflows
        page.add_style_tag(content="""
            body {
                width: 100%;                    // Make sure body width fits within the page
                max-width: 100vw;               // Prevent body from exceeding the viewport width
                margin: 0 auto;                 // Center content if needed
            }
            pre, code {
                white-space: pre-wrap;          // Wrap long lines of code or text to fit within the page
            }
            img, table {
                max-width: 100%;                // Ensure images and tables are not wider than the page
                height: auto;                   // Maintain aspect ratio for images
            }
        """)

        # Generate a PDF of the loaded page with the new styles
        page.pdf(path=output_pdf, format="A4", print_background=True)  # Include background styles

        # Close the browser after generating the PDF
        browser.close()
        
        print(f"PDF saved as {output_pdf}")

if __name__ == "__main__":
    # Take input URL from the user
    link = input(f"Please insert the link to download as pdf: \n")
    pdf_name = link.split('/')[-1]
    output_pdf = f"{pdf_name}.pdf"
    
    # Call the function to fetch the page and save it as PDF
    fetch_and_save_pdf(link, output_pdf)