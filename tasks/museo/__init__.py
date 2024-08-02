from resources import task_pixmaps_large, task_pixmaps_medium

title = "Museoscript"
description = "Turn matches into sequences"

pixmap = task_pixmaps_large.museo
pixmap_medium = task_pixmaps_medium.museo

long_description = (
    "Given a query file and a BLAST database, search the database for sequence matches, "
    "then create a sequence file from the hits. "
    "Query files must be in FASTA format. "
    "Output will consist of two files per query: the BLAST output and a FASTA file."
)
