import matplotlib.pyplot as plt

data_list = [{'generation': 1, 'data': [-1501, -1501, -1501, -1501, -1401, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1401, -1501, -1401, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1401, -1401, -1501, -1501, -1501, -1501, -1501, -1401, -1, -1501, -1501, -1501, 
-1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -101, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501]}, {'generation': 2, 'data': [-1501, -101, -1401, -1501, -1401, -1501, -1501, -1501, -1501, -1501, -1501, -1101, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1401, -1501, -1501, -1501, -1, -101, -1401, -1401, -1401, -1401, -1401, -1401, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501]}, {'generation': 3, 'data': [-1401, -1501, -1501, -1501, -1501, -1501, -1401, -1501, -1501, -1401, -1501, -1401, -1501, -101, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1, -101, -101, -1101, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501]}, {'generation': 4, 'data': [4399, -1501, -601, 999, -1501, -1501, -1401, -1501, -1401, -1401, -1501, -1401, -1401, -1401, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, 4299, -1501, -1501, -1501, -1501, -1501, -1501, -1401, -1501, -1501, -1501, -1501, -1, -101, -101, -101, -1101, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501]}, {'generation': 5, 'data': [4399, 4299, 999, -1501, -1501, -1501, 5107, -1501, -601, -1501, -101, -1501, -1501, -1501, -1401, -1501, -1501, -1301, -1501, -1501, -601, -1401, -1401, -1501, -1401, -1401, -1401, -1501, -1501, -1401, -1501, 5645, -1501, -1501, -1501, -1401, -1501, -1501, -1501, -1501, -1501, -1501, 3599, -1, -101, -101, 
-101, -601, -1101, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501, -1501]}, {'generation': 6, 'data': [5645, 5107, 4399, 4299, 3599, 999, -1501, 5542, -1501, -1501, 5601, -1501, -1501, -601, -101, -601, -1501, -601, -1501, -1501, -1501, -1501, -1501, -1501, -1401, -1501, -1401, -1501, -1501, -1501, -1401, -1501, -1401, -1501, -1501, -1401, -1501, -501, -1501, -1501, -1501, -1501, -1501, -1501, -1401, -1401, -1, -101, -101, -101, -101, -601, -601, -601, -1101, -1301, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401]}, {'generation': 7, 'data': [5645, 5601, 5542, 5107, 4399, 4299, 3599, 999, -1401, -1501, -1501, -1501, -1501, 999, -1501, 3199, -1501, -1501, -1501, -101, 1699, 5624, -501, -1501, 999, 199, -1501, -1501, -1501, -1001, -1401, -1501, -1401, -1401, -1501, -1501, -1401, -1401, -1401, -1401, -1401, -1401, -1501, -1401, -1501, -1401, -1401, -1401, -1, -101, -101, -101, -101, -101, -501, -601, -601, -601, -601, -601, -601, -1101, -1301, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401]}, {'generation': 8, 'data': [5645, 5624, 5601, 5542, 5107, 4399, 4299, 3599, 3199, 1699, 999, 999, 999, 199, 5683, -1501, -1501, -1501, 5252, 2699, 3199, 5564, -1501, 2699, -1501, -1501, -1501, -1501, 5523, -601, 5484, -101, -1501, -601, -1501, -101, -801, -1501, -1501, -601, -1501, -1501, -1501, -1501, -1501, -1501, -1401, -1401, -1401, -1401, -1501, -1301, -1401, -1401, -1, -101, -101, -101, -101, -101, -101, -501, -501, -601, -601, -601, -601, -601, -601, -1001, -1101, -1301, -1401, -1401, -1401, -1401, -1401, -1401, -1401, -1401]}, {'generation': 9, 'data': [5683, 5645, 5624, 5601, 5564, 5542, 5523, 5484, 5252, 5107, 4399, 4299, 3599, 3199, 3199, 2699, 2699, 1699, 999, 999, 999, 199, -1501, 1999, 5558, -1, -101, 5521, -1501, -1501, -601, 5251, -401, -1501, -1501, 3199, -1501, -1401, 2699, -1501, -1501, -1501, 199, -501, -501, -1401, -1501, -1501, -101, -1501, -1501, -1501, -1501, -1501, -1301, -601, -101, -601, -101, -501, -601, -1501, -1, -101, -101, -101, -101, -101, -101, -101, -101, -501, -501, -601, -601, -601, -601, -601, -601, -601]}, {'generation': 10, 'data': [5683, 5645, 5624, 5601, 5564, 5558, 5542, 5523, 5521, 5484, 5252, 5251, 5107, 4399, 4299, 3599, 3199, 3199, 3199, 2699, 2699, 2699, 1999, 1699, 999, 999, 999, 199, 199, 5627, -1401, 5628, -1501, -1501, -1501, 5523, -501, 5579, -1501, -1401, -1501, -1501, -1001, 5582, 5645, -1501, 999, -1501, -601, -1401, 2699, -1501, -1501, -601, -1501, -601, -601, 5497, -1401, -601, -1401, 5471, -1501, 1699, -1501, -1501, -1501, 999, 3099, -1, -1, -101, -101, -101, -101, -101, -101, -101, -101, -101]}, {'generation': 11, 'data': [5683, 5645, 5645, 5628, 5627, 5624, 5601, 5582, 5579, 5564, 5558, 5542, 5523, 5523, 5521, 5497, 5484, 5471, 5252, 5251, 5107, 4399, 4299, 3599, 3199, 3199, 3199, 3099, 2699, 2699, 2699, 2699, 1999, 1699, 1699, 999, 999, 999, 999, 999, 5619, 5683, 5614, -401, -401, -1501, 3599, -1501, 1499, 5533, -1, -1501, 5547, -901, -601, -1501, -1501, -1401, 5247, -1501, 5561, 1099, 5521, 999, -1501, -601, -1401, -1401, -601, 1099, 2699, -601, 1999, 1999, -1501, -1501, -1401, 999, -1501, -601]}, {'generation': 12, 'data': [5683, 5683, 5645, 5645, 5628, 5627, 5624, 5619, 5614, 5601, 5582, 5579, 5564, 5561, 5558, 5547, 5542, 5533, 5523, 5523, 5521, 5521, 5497, 5484, 5471, 5252, 5251, 5247, 5107, 4399, 4299, 3599, 3599, 3199, 3199, 
3199, 3099, 2699, 2699, 2699, -1501, 5683, 5631, -1401, 5566, -1501, 5496, 5563, -1501, -1501, 5514, -1401, 5561, -1501, 5567, 1599, 5542, -1501, 5523, -1501, 3599, 5480, -501, -1501, -1501, -1501, -1501, 
-1501, -1501, 5567, -1501, -1501, 3599, -1401, -401, 1599, -1501, -501, -1501, -601]}, {'generation': 13, 'data': [5683, 5683, 5683, 5645, 5645, 5631, 5628, 5627, 5624, 5619, 5614, 5601, 5582, 5579, 5567, 
5567, 5566, 5564, 5563, 5561, 5561, 5558, 5547, 5542, 5542, 5533, 5523, 5523, 5523, 5521, 5521, 5514, 5497, 5496, 5484, 5480, 5471, 5252, 5251, 5247, 5565, 1099, 5568, 5674, -1501, 5001, 5626, 5512, 5682, 
5699, 3599, -1501, 5531, 5525, -1501, 5602, 5531, -401, -1501, 299, -1401, 5623, -1001, -1501, 5651, -101, 5490, 5523, 1499, -1501, 1599, -401, -1501, 5497, 5537, -1501, 5471, -1501, 5271, -1501]}, {'generation': 14, 'data': [5699, 5683, 5683, 5683, 5682, 5674, 5651, 5645, 5645, 5631, 5628, 5627, 5626, 5624, 5623, 5619, 5614, 5602, 5601, 5582, 5579, 5568, 5567, 5567, 5566, 5565, 5564, 5563, 5561, 5561, 5558, 5547, 5542, 5542, 5537, 5533, 5531, 5531, 5525, 5523, 5620, 5577, 5679, 5606, 99, -1501, -401, -1501, 1899, -601, 1199, 5577, 5622, 1499, -1501, -1501, -1501, -1501, -1501, -401, -1501, -1501, -1501, -1501, -1501, 5565, 5517, 5568, 5528, -1, 5577, -1501, -1401, 1599, -1501, -1501, 2599, 5531, 5525, 5523]}, {'generation': 15, 'data': [5699, 5683, 5683, 5683, 5682, 5679, 5674, 5651, 5645, 5645, 5631, 5628, 
5627, 5626, 5624, 5623, 5622, 5620, 5619, 5614, 5606, 5602, 5601, 5582, 5579, 5577, 5577, 5577, 5568, 5568, 5567, 5567, 5566, 5565, 5565, 5564, 5563, 5561, 5561, 5558, 1099, -401, 5596, -1501, -401, 5682, 
1599, -1501, 299, 5593, 5515, 5613, 3699, -1501, 5640, -1401, -1501, -1, 4399, -1, -1001, 5665, 1599, 5537, -1501, 5527, 99, 2599, -1501, -1501, -1501, -801, -1501, 5676, 5623, 4699, -1501, -1501, 5561, 5566]}, {'generation': 16, 'data': [5699, 5683, 5683, 5683, 5682, 5682, 5679, 5676, 5674, 5665, 5651, 5645, 5645, 5640, 5631, 5628, 5627, 5626, 5624, 5623, 5623, 5622, 5620, 5619, 5614, 5613, 5606, 5602, 5601, 5596, 5593, 5582, 5579, 5577, 5577, 5577, 5568, 5568, 5567, 5567, 5624, 1199, 5545, 3599, 4399, 5633, -1501, -1501, 4399, 2699, 5645, 5530, -601, -1501, -1501, 2799, 2599, 1099, -1401, 5588, -1501, 1699, 1599, -1401, -501, 5612, -1501, -501, 5510, -801, -1, 5571, 4199, 3199, 5577, 5613, 3099, -601, -1501, 5542]}, {'generation': 17, 'data': [5699, 5683, 5683, 5683, 5682, 5682, 5679, 5676, 5674, 5665, 5651, 5645, 5645, 5645, 5640, 5633, 5631, 5628, 5627, 5626, 5624, 5624, 5623, 5623, 5622, 5620, 5619, 5614, 5613, 5613, 5612, 5606, 5602, 5601, 5596, 5593, 5588, 5582, 5579, 5577, 5689, -1501, 5683, 5683, 5681, 5680, 1199, 1199, 5619, -1, 5596, 5623, 5532, -1501, -1501, 4399, -1501, 4399, 5679, -1501, -401, 1599, 5609, 5627, -1501, 5556, 3199, -401, -601, -1501, -601, 5606, -1401, 5590, 5626, 5499, -401, -101, 
5577, 5539]}, {'generation': 18, 'data': [5699, 5689, 5683, 5683, 5683, 5683, 5683, 5682, 5682, 5681, 5680, 5679, 5679, 5676, 5674, 5665, 5651, 5645, 5645, 5645, 5640, 5633, 5631, 5628, 5627, 5627, 5626, 5626, 5624, 5624, 5623, 5623, 5623, 5622, 5620, 5619, 5619, 5614, 5613, 5613, -1501, 5680, 5688, 5573, 5631, -501, 5509, -1501, 5544, 4299, 5537, -1501, 5564, 5554, 5565, 1199, 3599, 1599, 5589, 5625, 1999, 5580, -401, -1501, -1501, -1401, -1501, -1501, -401, -1501, -1501, -1501, 299, 1999, 5605, 5598, 5667, -201, -101, 4299]}, {'generation': 19, 'data': [5699, 5689, 5688, 5683, 5683, 5683, 5683, 5683, 5682, 5682, 5681, 5680, 5680, 5679, 5679, 5676, 5674, 5667, 5665, 5651, 5645, 5645, 5645, 5640, 5633, 5631, 5631, 5628, 5627, 5627, 5626, 5626, 5625, 5624, 5624, 5623, 5623, 5623, 5622, 5620, -1501, 5482, 1599, -1501, 1099, -1, 5587, -1501, 5682, 5678, 4599, -1501, 3299, 4299, 5679, 5672, 1699, -1501, 1099, 2599, -1501, -1501, 1599, 1599, -1501, 1599, 2799, -1501, 5630, 5651, -1501, 5582, -1501, 2799, 1599, -401, 5717, -501, 5552, 5665]}, {'generation': 20, 'data': [5717, 5699, 5689, 5688, 5683, 5683, 5683, 5683, 5683, 5682, 5682, 5682, 5681, 5680, 5680, 5679, 5679, 5679, 5678, 5676, 5674, 5672, 5667, 5665, 5665, 5651, 5651, 5645, 5645, 5645, 5640, 5633, 5631, 5631, 5630, 5628, 5627, 5627, 5626, 5626, 5570, 5541, -1501, -1501, 1599, 5667, -1501, 5680, 5603, -1501, -1501, 1199, -601, 5682, 3499, 5592, 3199, 5680, 5535, 5682, 299, 5534, -1501, 5557, -401, -1501, 5584, 5537, -1501, -1, -1, -1501, -1501, -1501, 1199, -1501, 5680, 2799, 5624, 5632]}, {'generation': 21, 'data': [5717, 5699, 5689, 5688, 5683, 5683, 5683, 
5683, 5683, 5682, 5682, 5682, 5682, 5682, 5681, 5680, 5680, 5680, 5680, 5680, 5679, 5679, 5679, 5678, 5676, 5674, 5672, 5667, 5667, 5665, 5665, 5651, 5651, 5645, 5645, 5645, 5640, 5633, 5632, 5631, -1, 5664, -1501, 3299, 5606, -1501, 1199, 5683, -1, 5554, 5623, -1501, -1501, 3599, 4399, 5625, -1501, -701, 5680, 5544, 4299, 5633, 5574, -501, 5621, 1099, -1501, 5684, 1599, 1599, 5651, 999, 5545, 5643, 1099, -601, 5612, 5633, -1501, 2799]}, {'generation': 22, 'data': [5717, 5699, 5689, 5688, 5684, 5683, 5683, 5683, 5683, 5683, 5683, 5682, 5682, 5682, 5682, 5682, 5681, 5680, 5680, 5680, 5680, 5680, 5680, 5679, 5679, 5679, 5678, 5676, 5674, 5672, 5667, 5667, 5665, 5665, 5664, 5651, 5651, 5651, 5645, 5645, 5718, 4299, -1, 3699, 5572, -701, 5623, -1501, 3499, 3299, 5725, 5681, -601, -1401, 1599, -1401, 5682, -501, -1501, -1501, -1501, 5680, 1599, 5521, 5679, 2799, -1501, 5546, 5672, -1501, 1599, -1501, 5583, 5663, 5585, 5533, -401, 5578, 5628, -1501]}, {'generation': 23, 'data': [5725, 5718, 5717, 5699, 5689, 5688, 5684, 5683, 5683, 5683, 5683, 5683, 5683, 5682, 5682, 5682, 5682, 5682, 5682, 5681, 5681, 5680, 5680, 5680, 5680, 5680, 5680, 5680, 5679, 5679, 5679, 5679, 5678, 5676, 5674, 5672, 5672, 5667, 5667, 5665, 4299, 5615, -1501, -1501, 1599, -1501, 5663, 1499, -1501, 5667, 5680, -501, -1501, -1501, -1, 5632, 5692, 5489, 5682, 5617, 5517, 5684, -1501, 5594, 4199, 1199, 5680, 5145, -1501, 5588, 5580, 5679, 1199, 5621, 5672, 5531, -1501, 1599, 5665, 5680]}]
# Extract x and y values
generations = [entry['generation'] for entry in data_list]
y_values = [entry['data'] for entry in data_list]

# Plot
plt.figure(figsize=(10, 6))
for i, y in enumerate(y_values):
    plt.plot(generations, y, label=f'Generation {i+1}')

# Add labels and title
plt.xlabel('Generation')
plt.ylabel('Data')
plt.title('Data Plot')
plt.legend()
plt.grid(True)

# Show plot
plt.show()