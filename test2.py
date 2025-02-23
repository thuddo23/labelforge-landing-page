# import dns.resolver
#
#
# def get_smtp_server(email):
#     try:
#         # Extract domain from email
#         domain = email.split('@')[-1]
#
#         # Query MX records
#         answers = dns.resolver.resolve(domain, 'MX')
#
#         # Get the first MX record (highest priority)
#         mx_record = sorted(answers, key=lambda x: x.preference)[0]
#
#         # Extract SMTP server
#         smtp_server = str(mx_record.exchange).rstrip('.')
#
#         return smtp_server
#     except Exception as e:
#         return f"Error: {e}"
#
#
# # Example usage
# emails = [
#     "hungnd@apero.vn",
#     "quyetnm@ikameglobal.com",
#     "admin@labelforge.tech",
# ]
# for email in emails:
#     smtp_server = get_smtp_server(email)
#     print(f"SMTP Server for {email}: {smtp_server}")
