import tkinter as tk
import tkinter.messagebox as messagebox
import smtplib

def send_email():
    sender_email = sender_entry.get()
    password = password_entry.get()
    receiver_email = receiver_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)

        full_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, receiver_email, full_message)

        server.quit()
        messagebox.showinfo("Success", "Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Error", "Authentication failed. Check your credentials.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("SB Mailer")


sender_label = tk.Label(root, text="Sender Email:")
sender_label.pack()
sender_entry = tk.Entry(root)
sender_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

receiver_label = tk.Label(root, text="Receiver Email:")
receiver_label.pack()
receiver_entry = tk.Entry(root)
receiver_entry.pack()

subject_label = tk.Label(root, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(root)
subject_entry.pack()

message_label = tk.Label(root, text="Message:")
message_label.pack()
message_text = tk.Text(root, wrap=tk.WORD)
message_text.pack()

send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.pack()

root.mainloop()
