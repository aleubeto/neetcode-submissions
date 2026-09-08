public class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        return useHashMap(s, t);
    }

    private boolean useHashMap(String s, String t) {
        HashMap<Character, Integer> dictS = new HashMap<>();
        HashMap<Character, Integer> dictT = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            dictS.put(s.charAt(i), dictS.getOrDefault(s.charAt(i), 0) + 1);
            dictT.put(t.charAt(i), dictT.getOrDefault(t.charAt(i), 0) + 1);
        }
        return dictS.equals(dictT);
    }
}