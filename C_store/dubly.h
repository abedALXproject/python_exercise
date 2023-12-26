#ifndef DUBLY.H
#define DUBLY.H

Typedef struct inno_s {
	int me;
	struct inno_s *next;
	struct inno_s *prev;
}inno_t;

inno_t mefirst_n(inno_s me, inno_s *next; inno_s *prev);
#endif
