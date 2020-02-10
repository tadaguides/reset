"""
https://leetcode.com/problems/unique-email-addresses/
Intuition and Algorithm
- For each email address, convert it to the canonical address that actually receives the mail. This involves a few steps:
- Separate the email address into a local part and the rest of the address.
- If the local part has a '+' character, remove it and everything beyond it from the local part.
- Remove all the zeros from the local part.
- The canonical address is local + rest.
- After, we can count the number of unique canonical addresses with a Set structure.
"""

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uniqueEmails = set()
        for email in emails:
            front, back = email.split("@")
            if "+" in front:
                front = front[:front.find("+")]
            uniqueEmails.add("@".join([front.replace(".",""),back]))
        return len(uniqueEmails)

if __name__ == "__main__":
    s = Solution()
    #emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    emails = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
    print s.numUniqueEmails(emails)