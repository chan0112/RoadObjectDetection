  *	$??sK?@2x
AIterator::Root::BatchV2::Prefetch::Shuffle::Zip[0]::ParallelMapV2(?{G?	0@!?`?jx?H@)?{G?	0@1?`?jx?H@:Preprocessing2N
Iterator::Root::BatchV2p???m.@!???Q??G@)B|`?? @1s???>1:@:Preprocessing2X
!Iterator::Root::BatchV2::Prefetch ???XPH@!{%??H5@)???XPH@1{%??H5@:Preprocessing2f
/Iterator::Root::BatchV2::Prefetch::Shuffle::Zip(6[y??|0@!?n?H??I@)T??Yh???1`cM=???:Preprocessing2?
NIterator::Root::BatchV2::Prefetch::Shuffle::Zip[1]::ParallelMapV2::TensorSlice(?Z`?????!?,[w???)?Z`?????1?,[w???:Preprocessing2x
AIterator::Root::BatchV2::Prefetch::Shuffle::Zip[1]::ParallelMapV2(g`?eM,??!(uy??;??)g`?eM,??1(uy??;??:Preprocessing2a
*Iterator::Root::BatchV2::Prefetch::Shuffle(+2: 	?0@!-8???I@)E???V	??1???L?O??:Preprocessing2?
NIterator::Root::BatchV2::Prefetch::Shuffle::Zip[0]::ParallelMapV2::TensorSlice(p?71$'??!??????)p?71$'??1??????:Preprocessing2E
Iterator::Root??;3?p.@!wS?(c?G@)>?4a??x?1u?C6?V??:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysisk
unknownTNo step time measured. Therefore we cannot tell where the performance bottleneck is.no*noZno#You may skip the rest of this page.BZ
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown
  " * 2 : B J R Z b JGPUb??No step marker observed and hence the step time is unknown. This may happen if (1) training steps are not instrumented (e.g., if you are not using Keras) or (2) the profiling duration is shorter than the step time. For (1), you need to add step instrumentation; for (2), you may try to profile longer.