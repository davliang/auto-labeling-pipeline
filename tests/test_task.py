import pytest

from auto_labeling_pipeline.label import ClassificationLabel, Seq2seqLabel, SequenceLabel
from auto_labeling_pipeline.labels import ClassificationLabels, Seq2seqLabels, SequenceLabels
from auto_labeling_pipeline.task import DocumentClassification, Seq2seq, SequenceLabeling


@pytest.mark.parametrize(
    'task, expected',
    [
        (DocumentClassification, ClassificationLabel),
        (SequenceLabeling, SequenceLabel),
        (Seq2seq, Seq2seqLabel)
    ]
)
def test_return_correct_label_class(task, expected):
    assert task.label_class == expected


@pytest.mark.parametrize(
    'task, expected',
    [
        (DocumentClassification, ClassificationLabels),
        (SequenceLabeling, SequenceLabels),
        (Seq2seq, Seq2seqLabels)
    ]
)
def test_return_correct_label_collection(task, expected):
    assert task.label_collection == expected
