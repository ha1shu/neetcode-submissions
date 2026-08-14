class Solution {
    public int characterReplacement(String s, int k) {
        int[] freq = new int[26];
        int left = 0, maxFreq = 0, maxLen = 0;

        for (int right = 0; right < s.length(); right++) {
            int idx = s.charAt(right) - 'A';
            freq[idx]++;

            
            maxFreq = Math.max(maxFreq, freq[idx]);

            int windowLen = right - left + 1;

            
            if (windowLen - maxFreq > k) {
                freq[s.charAt(left) - 'A']--;
                left++;
            } else {
                maxLen = Math.max(maxLen, windowLen);
            }
        }

        return maxLen;
    }
}
