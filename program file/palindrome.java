public class PalindromeChecker {

    public static void main(String[] args) {
        // Test strings
        String[] testStrings = {"racecar", "hello", "A man, a plan, a canal, Panama", "No 'x' in Nixon"};

        for (String str : testStrings) {
            if (isPalindrome(str)) {
                System.out.println("\"" + str + "\" is a palindrome.");
            } else {
                System.out.println("\"" + str + "\" is not a palindrome.");
            }
        }
    }

    public static boolean isPalindrome(String s) {
        // Remove non-alphanumeric characters and convert to lower case
        String cleanedString = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int left = 0;
        int right = cleanedString.length() - 1;

        while (left < right) {
            if (cleanedString.charAt(left) != cleanedString.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}