  *	????J??@2x
AIterator::Root::BatchV2::Prefetch::Shuffle::Zip[0]::ParallelMapV2(?????-@!?k????F@)?????-@1?k????F@:Preprocessing2N
Iterator::Root::BatchV2??A?1@!??4J@)???"@1??dO?<@:Preprocessing2X
!Iterator::Root::BatchV2::Prefetch XT??$?@!a??`v7@)XT??$?@1a??`v7@:Preprocessing2f
/Iterator::Root::BatchV2::Prefetch::Shuffle::Zip(??#??O.@!??˚?HG@)?ѩ+????1H?K*??:Preprocessing2?
NIterator::Root::BatchV2::Prefetch::Shuffle::Zip[1]::ParallelMapV2::TensorSlice(ղ??Hh??!???????)ղ??Hh??1???????:Preprocessing2x
AIterator::Root::BatchV2::Prefetch::Shuffle::Zip[1]::ParallelMapV2(a??????!`Rl.????)a??????1`Rl.????:Preprocessing2?
NIterator::Root::BatchV2::Prefetch::Shuffle::Zip[0]::ParallelMapV2::TensorSlice(?ʼUס??!?X??6u??)?ʼUס??1?X??6u??:Preprocessing2a
*Iterator::Root::BatchV2::Prefetch::Shuffle(H?????.@!?0q??nG@)?Վ?u??1!i?R????:Preprocessing2E
Iterator::Root???1@!*?čw>J@){.S????1C?h?>??:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysisk
unknownTNo step time measured. Therefore we cannot tell where the performance bottleneck is.no*noZno#You may skip the rest of this page.BZ
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown
  " * 2 : B J R Z b JGPUb??No step marker observed and hence the step time is unknown. This may happen if (1) training steps are not instrumented (e.g., if you are not using Keras) or (2) the profiling duration is shorter than the step time. For (1), you need to add step instrumentation; for (2), you may try to profile longer.