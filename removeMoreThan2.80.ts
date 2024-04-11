function removeDuplicates(nums: Number[]) {
  let elem = 0;
  let counter: { [key: number]: number } = {};
  let removeIndexes = [];
  for (let i = 0; i < nums.length; i++) {
    counter[nums[i]] = 0;
  }
  for (let j = 0; j < nums.length; j++) {
    if (counter[nums[j]] < 2) {
      counter[nums[j]]++;
      elem++;
    } else {
      removeIndexes.push(j);
    }
  }

  nums = nums.filter((_, i) => !removeIndexes.includes(i));
  console.log(removeIndexes);
  console.log(nums, elem);
  return elem;
}

removeDuplicates([1, 2, 3, 4, 5, 5, 5, 2, 2]);
