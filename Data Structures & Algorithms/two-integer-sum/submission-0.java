class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> indexes = new HashMap<>();
        for(int index = 0; index < nums.length; index++) {
            int diff = target - nums[index];
            if(indexes.containsKey(diff)){
                return new int[]{indexes.get(diff), index};
            } else {
                indexes.put(nums[index], index);
            }
        }
        return new int[0];
    }
}
