import qrcode

# Base URL of your live Render website
base_url = "https://course-system-mg00.onrender.com"

# Loop through stages 1 to 7 to generate everything automatically
for stage_num in range(1, 8):
    # 1. Create the unique link for each stage (e.g., /s1, /s2, etc.)
    stage_link = f"{base_url}/s{stage_num}"
    
    # 2. Generate the QR code
    img = qrcode.make(stage_link)
    
    # 3. Create a unique filename for each image (e.g., stage1_qr.png)
    filename = f"stage{stage_num}_qr.png"
    
    # 4. Save the image file to your folder
    img.save(filename)
    
    print(f"Generated QR code for Stage {stage_num} -> Saved as {filename}")

print("\n🎉 All 7 QR codes have been created successfully!")