syscall = {

    "chmod"                 : { "id": 0, "threat": 1 },
    "chown"                 : { "id": 1, "threat": 1 },
    "chown32"               : { "id": 2, "threat": 1 },
    "execveat"              : { "id": 3, "threat": 1 },
    "fanotify_init"         : { "id": 4, "threat": 1 },
    "fanotify_mark"         : { "id": 5, "threat": 1 }, 
    "fchmod"                : { "id": 6, "threat": 1 }, 
    "fchmodat"              : { "id": 7, "threat": 1 },
    "fchown"                : { "id": 8, "threat": 1 }, 
    "fchown32"              : { "id": 9, "threat": 1 }, 
    "fchownat"              : { "id": 10, "threat": 1 }, 
    "fsetxattr"             : { "id": 11, "threat": 1 }, 
    "fsmount"               : { "id": 12, "threat": 1 }, 
    "fsopen"                : { "id": 13, "threat": 1 }, 
    "lchown"                : { "id": 14, "threat": 1 }, 
    "lchown32"              : { "id": 15, "threat": 1 }, 
    "link"                  : { "id": 16, "threat": 1 }, 
    "linkat"                : { "id": 17, "threat": 1 },
    "lsetxattr"             : { "id": 18, "threat": 1 }, 
    "mount"                 : { "id": 19, "threat": 1 }, 
    "perf_event_open"       : { "id": 20, "threat": 1 }, 
    "pivot_root"            : { "id": 21, "threat": 1 }, 
    "rename"                : { "id": 22, "threat": 1 }, 
    "renameat"              : { "id": 23, "threat": 1 }, 
    "renameat2"             : { "id": 24, "threat": 1 }, 
    "setxattr"              : { "id": 25, "threat": 1 },
    "splice"                : { "id": 26, "threat": 1 }, 
    "symlink"               : { "id": 27, "threat": 1 }, 
    "symlinkat"             : { "id": 28, "threat": 1 }, 
    "tee"                   : { "id": 29, "threat": 1 }, 
    "unlink"                : { "id": 30, "threat": 1 }, 
    "unlinkat"              : { "id": 31, "threat": 1 }, 
    "userfaultfd"           : { "id": 32, "threat": 1 }, 
    "utimensat"             : { "id": 33, "threat": 1 }, 
    "vmsplice"              : { "id": 34, "threat": 1 },
    "execve"                : { "id": 35, "threat": 1 }, 
    "getresgid"             : { "id": 36, "threat": 1 }, 
    "getresgid32"           : { "id": 37, "threat": 1 }, 
    "getresuid"             : { "id": 38, "threat": 1 }, 
    "getresuid32"           : { "id": 39, "threat": 1 }, 
    "ioperm"                : { "id": 40, "threat": 1 }, 
    "keyctl"                : { "id": 41, "threat": 1 }, 
    "rseq"                  : { "id": 42, "threat": 1 }, 
    "seccomp"               : { "id": 43, "threat": 1 },
    "set_thread_area"       : { "id": 44, "threat": 1 }, 
    "set_tid_address"       : { "id": 45, "threat": 1 }, 
    "setfsgid"              : { "id": 46, "threat": 1 }, 
    "setfsgid32"            : { "id": 47, "threat": 1 }, 
    "setfsuid"              : { "id": 48, "threat": 1 }, 
    "setfsuid32"            : { "id": 49, "threat": 1 }, 
    "setgid"                : { "id": 50, "threat": 1 }, 
    "setgid32"              : { "id": 51, "threat": 1 }, 
    "setgroups"             : { "id": 52, "threat": 1 }, 
    "setgroups32"           : { "id": 53, "threat": 1 }, 
    "setpgid"               : { "id": 54, "threat": 1 }, 
    "setregid"              : { "id": 55, "threat": 1 }, 
    "setregid32"            : { "id": 56, "threat": 1 }, 
    "setresgid"             : { "id": 57, "threat": 1 }, 
    "setresgid32"           : { "id": 58, "threat": 1 }, 
    "setresuid"             : { "id": 59, "threat": 1 }, 
    "setresuid32"           : { "id": 60, "threat": 1 }, 
    "setreuid"              : { "id": 61, "threat": 1 }, 
    "setreuid32"            : { "id": 62, "threat": 1 }, 
    "setsid"                : { "id": 63, "threat": 1 }, 
    "setuid"                : { "id": 64, "threat": 1 }, 
    "setuid32"              : { "id": 65, "threat": 1 }, 
    "unshare"               : { "id": 66, "threat": 1 },
    "delete_module"         : { "id": 67, "threat": 1 }, 
    "finit_module"          : { "id": 68, "threat": 1 }, 
    "init_module"           : { "id": 69, "threat": 1 }, 
    "inotify_init"          : { "id": 70, "threat": 1 }, 
    "inotify_init1"         : { "id": 71, "threat": 1 }, 
    "request_key"           : { "id": 72, "threat": 1 },
    "modify_ldt"            : { "id": 73, "threat": 1 }, 
    "move_mount"            : { "id": 74, "threat": 1 }, 
    "move_pages"            : { "id": 75, "threat": 1 }, 
    "pkey_mprotect"         : { "id": 76, "threat": 1 }, 
    "process_vm_writev"     : { "id": 77, "threat": 1 },
    "getitimer"             : { "id": 78, "threat": 1 },
    "accept"                : { "id": 79, "threat": 1 }, 
    "accept6"               : { "id": 80, "threat": 1 }, 
    "mq_getsetattr"         : { "id": 81, "threat": 1 },
    "pkey_alloc"            : { "id": 82, "threat": 1 }, 
    "pkey_free"             : { "id": 83, "threat": 1 }, 
    "restart_syscall"       : { "id": 84, "threat": 1 }, 
    "semctl"                : { "id": 85, "threat": 1 }, 
    "setns"                 : { "id": 86, "threat": 1 }, 
    "setpriority"           : { "id": 87, "threat": 1 }, 
    "sethostid"             : { "id": 88, "threat": 1 },
    "create_module"         : { "id": 89, "threat": 1 },
    "ioctl"                 : { "id": 90, "threat": 1 }, 
    "iopl"                  : { "id": 91, "threat": 1 }, 
    "epoll"                 : { "id": 92, "threat": 1 },
    "_llseek"               : { "id": 93, "threat": 2 },
    "chdir"                 : { "id": 94, "threat": 2 }, 
    "chroot"                : { "id": 95, "threat": 2 }, 
    "epoll_ctl"             : { "id": 96, "threat": 2 }, 
    "fcntl"                 : { "id": 97, "threat": 2 }, 
    "fcntl64"               : { "id": 98, "threat": 2 }, 
    "ftruncate"             : { "id": 99, "threat": 2 }, 
    "ftruncate64"           : { "id": 100, "threat": 2 }, 
    "lseek"                 : { "id": 101, "threat": 2 }, 
    "mkdir"                 : { "id": 102, "threat": 2 },
    "mkdirat"               : { "id": 103, "threat": 2 }, 
    "mknod"                 : { "id": 104, "threat": 2 }, 
    "mknodat"               : { "id": 105, "threat": 2 }, 
    "pread"                 : { "id": 106, "threat": 2 }, 
    "pread64"               : { "id": 107, "threat": 2 }, 
    "preadv"                : { "id": 108, "threat": 2 }, 
    "preadv2"               : { "id": 109, "threat": 2 }, 
    "pwritev"               : { "id": 110, "threat": 2 }, 
    "pwritev2"              : { "id": 111, "threat": 2 }, 
    "readv"                 : { "id": 112, "threat": 2 },
    "sync_file_range"       : { "id": 113, "threat": 2 },
    "sync_file_range2"      : { "id": 114, "threat": 2 }, 
    "syncfs"                : { "id": 115, "threat": 2 }, 
    "truncate"              : { "id": 116, "threat": 2 }, 
    "truncate64"            : { "id": 117, "threat": 2 }, 
    "umask"                 : { "id": 118, "threat": 2 }, 
    "utime"                 : { "id": 119, "threat": 2 }, 
    "utimes"                : { "id": 120, "threat": 2 },
    "write"                 : { "id": 121, "threat": 2 }, 
    "writev"                : { "id": 122, "threat": 2 }, 
    "epoll_ctl_old"         : { "id": 123, "threat": 2 },
    "arch_prctl"            : { "id": 124, "threat": 2 }, 
    "capset"                : { "id": 125, "threat": 2 }, 
    "exit"                  : { "id": 126, "threat": 2 }, 
    "exit_group"            : { "id": 127, "threat": 2 }, 
    "fadvise64"             : { "id": 128, "threat": 2 }, 
    "fadvise64_64"          : { "id": 129, "threat": 2 }, 
    "fchdir"                : { "id": 130, "threat": 2 }, 
    "personality"           : { "id": 131, "threat": 2 },
    "prctl"                 : { "id": 132, "threat": 2 }, 
    "rt_sigaction"          : { "id": 133, "threat": 2 }, 
    "rt_sigpending"         : { "id": 134, "threat": 2 }, 
    "rt_sigprocmask"        : { "id": 135, "threat": 2 }, 
    "rt_sigqueueinfo"       : { "id": 136, "threat": 2 }, 
    "rt_sigreturn"          : { "id": 137, "threat": 2 },
    "rt_sigsuspend"         : { "id": 138, "threat": 2 }, 
    "rt_sigtimedwait"       : { "id": 139, "threat": 2 }, 
    "rt_tgsigqueueinfo"     : { "id": 140, "threat": 2 }, 
    "sched_yield"           : { "id": 141, "threat": 2 }, 
    "sigaction"             : { "id": 142, "threat": 2 }, 
    "sigaltstack"           : { "id": 143, "threat": 2 },
    "signal"                : { "id": 144, "threat": 2 }, 
    "signalfd"              : { "id": 145, "threat": 2 }, 
    "signalfd4"             : { "id": 146, "threat": 2 }, 
    "sigpending"            : { "id": 147, "threat": 2 }, 
    "sigprocmask"           : { "id": 148, "threat": 2 }, 
    "sigreturn"             : { "id": 149, "threat": 2 }, 
    "sigsuspend"            : { "id": 150, "threat": 2 }, 
    "ssetmask"              : { "id": 151, "threat": 2 },
    "uselib"                : { "id": 152, "threat": 2 }, 
    "wait4"                 : { "id": 153, "threat": 2 }, 
    "waitid"                : { "id": 154, "threat": 2 }, 
    "waitpid"               : { "id": 155, "threat": 2 },
    "add_key"               : { "id": 156, "threat": 2 }, 
    "inotify_add_watch"     : { "id": 157, "threat": 2 }, 
    "inotify_rm_watch"      : { "id": 158, "threat": 2 },
    "brk"                   : { "id": 159, "threat": 2 }, 
    "mprotect"              : { "id": 160, "threat": 2 }, 
    "mremap"                : { "id": 161, "threat": 2 }, 
    "munmap"                : { "id": 162, "threat": 2 }, 
    "sbrk"                  : { "id": 163, "threat": 2 },
    "clock_nanosleep"       : { "id": 164, "threat": 2 }, 
    "clock_settime"         : { "id": 165, "threat": 2 }, 
    "io_pgetevents"         : { "id": 166, "threat": 2 }, 
    "nanosleep"             : { "id": 167, "threat": 2 }, 
    "nice"                  : { "id": 168, "threat": 2 }, 
    "setitimer"             : { "id": 169, "threat": 2 }, 
    "timer_create"          : { "id": 170, "threat": 2 },
    "timer_delete"          : { "id": 171, "threat": 2 }, 
    "timer_settime"         : { "id": 172, "threat": 2 }, 
    "timerfd_create"        : { "id": 173, "threat": 2 }, 
    "timerfd_settime"       : { "id": 174, "threat": 2 },
    "connect"               : { "id": 175, "threat": 2 }, 
    "mq_notify"             : { "id": 176, "threat": 2 }, 
    "mq_open"               : { "id": 177, "threat": 2 }, 
    "msgctl"                : { "id": 178, "threat": 2 },
    "semget"                : { "id": 179, "threat": 2 }, 
    "semop"                 : { "id": 180, "threat": 2 }, 
    "semtimedop"            : { "id": 181, "threat": 2 },
    "_sysctl"               : { "id": 182, "threat": 2 },
    "io_cancel"             : { "id": 183, "threat": 2 }, 
    "io_destroy"            : { "id": 184, "threat": 2 }, 
    "io_getevents"          : { "id": 185, "threat": 2 }, 
    "io_setup"              : { "id": 186, "threat": 2 }, 
    "io_submit"             : { "id": 187, "threat": 2 }, 
    "io_uring_enter"        : { "id": 188, "threat": 2 },
    "io_uring_register"     : { "id": 189, "threat": 2 }, 
    "io_uring_setup"        : { "id": 190, "threat": 2 }, 
    "msync"                 : { "id": 191, "threat": 2 }, 
    "poll"                  : { "id": 192, "threat": 2 }, 
    "ppoll"                 : { "id": 193, "threat": 2 },
    "creat"                 : { "id": 194, "threat": 3 }, 
    "dup"                   : { "id": 195, "threat": 3 }, 
    "dup2"                  : { "id": 196, "threat": 3 }, 
    "dup3"                  : { "id": 197, "threat": 3 }, 
    "epoll_create"          : { "id": 198, "threat": 3 }, 
    "epoll_create1"         : { "id": 199, "threat": 3 }, 
    "eventfd"               : { "id": 200, "threat": 3 }, 
    "eventfd2"              : { "id": 201, "threat": 3 }, 
    "fallocate"             : { "id": 202, "threat": 3 },
    "flock"                 : { "id": 203, "threat": 3 }, 
    "fremovexattr"          : { "id": 204, "threat": 3 }, 
    "lremovexattr"          : { "id": 205, "threat": 3 }, 
    "name_to_handle_at"     : { "id": 206, "threat": 3 }, 
    "open"                  : { "id": 207, "threat": 3 }, 
    "open_by_handle_at"     : { "id": 208, "threat": 3 },
    "open_tree"             : { "id": 209, "threat": 3 }, 
    "openat"                : { "id": 210, "threat": 3 }, 
    "openat2"               : { "id": 211, "threat": 3 }, 
    "pidfd_getfd"           : { "id": 212, "threat": 3 }, 
    "pidfd_open"            : { "id": 213, "threat": 3 }, 
    "quotactl"              : { "id": 214, "threat": 3 }, 
    "read"                  : { "id": 215, "threat": 3 }, 
    "readahead"             : { "id": 216, "threat": 3 }, 
    "removexattr"           : { "id": 217, "threat": 3 }, 
    "rmdir"                 : { "id": 218, "threat": 3 }, 
    "sendfile"              : { "id": 219, "threat": 3 }, 
    "sendfile64"            : { "id": 220, "threat": 3 }, 
    "umount"                : { "id": 221, "threat": 3 }, 
    "umount2"               : { "id": 222, "threat": 3 },
    "bind"                  : { "id": 223, "threat": 3 }, 
    "clone2"                : { "id": 224, "threat": 3 }, 
    "clone"                 : { "id": 225, "threat": 3 }, 
    "clone3"                : { "id": 226, "threat": 3 }, 
    "futex"                 : { "id": 227, "threat": 3 }, 
    "getrlimit"             : { "id": 228, "threat": 3 }, 
    "kill"                  : { "id": 229, "threat": 3 }, 
    "prlimit64"             : { "id": 230, "threat": 3 }, 
    "ptrace"                : { "id": 231, "threat": 3 }, 
    "reboot"                : { "id": 232, "threat": 3 },
    "sched_setaffinity"     : { "id": 233, "threat": 3 }, 
    "sched_setattr"         : { "id": 234, "threat": 3 }, 
    "sched_setparam"        : { "id": 235, "threat": 3 }, 
    "sched_setscheduler"    : { "id": 236, "threat": 3 }, 
    "set_robust_list"       : { "id": 237, "threat": 3 },
    "setrlimit"             : { "id": 238, "threat": 3 }, 
    "fork"                  : { "id": 239, "threat": 3 }, 
    "vfork"                 : { "id": 240, "threat": 3 }, 
    "vhangup"               : { "id": 241, "threat": 3 }, 
    "vm86old"               : { "id": 242, "threat": 3 }, 
    "vm86"                  : { "id": 243, "threat": 3 }, 
    "_exit"                 : { "id": 244, "threat": 3 }, 
    "__clone2"              : { "id": 245, "threat": 3 },
    "madvise"               : { "id": 246, "threat": 3 }, 
    "mbind"                 : { "id": 247, "threat": 3 }, 
    "mincore"               : { "id": 248, "threat": 3 }, 
    "mlock"                 : { "id": 249, "threat": 3 }, 
    "mlock2"                : { "id": 250, "threat": 3 }, 
    "mlockall"              : { "id": 251, "threat": 3 }, 
    "mmap"                  : { "id": 252, "threat": 3 }, 
    "mmap2"                 : { "id": 253, "threat": 3 }, 
    "munlock"               : { "id": 254, "threat": 3 }, 
    "munlockall"            : { "id": 255, "threat": 3 },
    "process_vm_readv"      : { "id": 256, "threat": 3 }, 
    "set_mempolicy"         : { "id": 257, "threat": 3 }, 
    "swapoff"               : { "id": 258, "threat": 3 }, 
    "swapon"                : { "id": 259, "threat": 3 },
    "adjtimex"              : { "id": 260, "threat": 3 }, 
    "clock_adjtime"         : { "id": 261, "threat": 3 }, 
    "pause"                 : { "id": 262, "threat": 3 }, 
    "settimeofday"          : { "id": 263, "threat": 3 }, 
    "stime"                 : { "id": 264, "threat": 3 }, 
    "ntp_adjtime"           : { "id": 265, "threat": 3 },
    "bpf"                   : { "id": 266, "threat": 3 }, 
    "listen"                : { "id": 267, "threat": 3 }, 
    "mq_timedreceive"       : { "id": 268, "threat": 3 }, 
    "mq_timedsend"          : { "id": 269, "threat": 3 }, 
    "mq_unlink"             : { "id": 270, "threat": 3 }, 
    "msgrcv"                : { "id": 271, "threat": 3 }, 
    "msgsnd"                : { "id": 272, "threat": 3 },
    "pidfd_send_signal"     : { "id": 273, "threat": 3 }, 
    "recv"                  : { "id": 274, "threat": 3 }, 
    "recvfrom"              : { "id": 275, "threat": 3 }, 
    "recvmsg"               : { "id": 276, "threat": 3 }, 
    "recvmmsg"              : { "id": 277, "threat": 3 }, 
    "send"                  : { "id": 278, "threat": 3 }, 
    "sendmmsg"              : { "id": 279, "threat": 3 }, 
    "sendmsg"               : { "id": 280, "threat": 3 },
    "sendto"                : { "id": 281, "threat": 3 }, 
    "setsockopt"            : { "id": 282, "threat": 3 }, 
    "socket"                : { "id": 283, "threat": 3 }, 
    "socketcall"            : { "id": 284, "threat": 3 }, 
    "socketpair"            : { "id": 285, "threat": 3 }, 
    "killpg"                : { "id": 286, "threat": 3 }, 
    "raise"                 : { "id": 287, "threat": 3 },
    "fspick"                : { "id": 288, "threat": 3 }, 
    "setdomainname"         : { "id": 289, "threat": 3 }, 
    "sethostname"           : { "id": 290, "threat": 3 }, 
    "syslog"                : { "id": 291, "threat": 3 }, 
    "tgkill"                : { "id": 292, "threat": 3 }, 
    "tkill"                 : { "id": 293, "threat": 3 }, 
    "gethostid"             : { "id": 294, "threat": 3 }, 
    "ssize_t"               : { "id": 295, "threat": 3 },
    "nfsservctl"            : { "id": 296, "threat": 3 },
    "pselect6"              : { "id": 297, "threat": 3 }, 
    "select"                : { "id": 298, "threat": 3 },
    "close"                 : { "id": 299, "threat": 4 }, 
    "copy_file_range"       : { "id": 300, "threat": 4 }, 
    "fgetxattr"             : { "id": 301, "threat": 4 }, 
    "getdents"              : { "id": 302, "threat": 4 }, 
    "getdents64"            : { "id": 303, "threat": 4 }, 
    "getxattr"              : { "id": 304, "threat": 4 }, 
    "lgetxattr"             : { "id": 305, "threat": 4 }, 
    "listxattr"             : { "id": 306, "threat": 4 },
    "llistxattr"            : { "id": 307, "threat": 4 }, 
    "lookup_dcookie"        : { "id": 308, "threat": 4 }, 
    "lstat"                 : { "id": 309, "threat": 4 }, 
    "lstat64"               : { "id": 310, "threat": 4 }, 
    "newfstatat"            : { "id": 311, "threat": 4 }, 
    "oldfstat"              : { "id": 312, "threat": 4 }, 
    "oldlstat"              : { "id": 313, "threat": 4 }, 
    "oldstat"               : { "id": 314, "threat": 4 }, 
    "pipe"                  : { "id": 315, "threat": 4 },
    "pipe2"                 : { "id": 316, "threat": 4 }, 
    "readdir"               : { "id": 317, "threat": 4 }, 
    "readlink"              : { "id": 318, "threat": 4 }, 
    "readlinkat"            : { "id": 319, "threat": 4 }, 
    "stat"                  : { "id": 320, "threat": 4 }, 
    "stat64"                : { "id": 321, "threat": 4 }, 
    "statfs"                : { "id": 322, "threat": 4 }, 
    "statfs64"              : { "id": 323, "threat": 4 }, 
    "statx"                 : { "id": 324, "threat": 4 }, 
    "sync"                  : { "id": 325, "threat": 4 }, 
    "sysfs"                 : { "id": 326, "threat": 4 }, 
    "ustat"                 : { "id": 327, "threat": 4 },
    "access"                : { "id": 328, "threat": 4 }, 
    "acct"                  : { "id": 329, "threat": 4 }, 
    "alarm"                 : { "id": 330, "threat": 4 }, 
    "capget"                : { "id": 331, "threat": 4 }, 
    "cmpxchg_badaddr"       : { "id": 332, "threat": 4 }, 
    "faccessat"             : { "id": 333, "threat": 4 }, 
    "flistxattr"            : { "id": 334, "threat": 4 }, 
    "fstat"                 : { "id": 335, "threat": 4 }, 
    "fstat64"               : { "id": 336, "threat": 4 }, 
    "fstatat64"             : { "id": 337, "threat": 4 }, 
    "fstatfs"               : { "id": 338, "threat": 4 }, 
    "fstatfs64"             : { "id": 339, "threat": 4 }, 
    "get_robust_list"       : { "id": 340, "threat": 4 }, 
    "getcpu"                : { "id": 341, "threat": 4 }, 
    "getcwd"                : { "id": 342, "threat": 4 }, 
    "getegid"               : { "id": 343, "threat": 4 }, 
    "getegid32"             : { "id": 344, "threat": 4 }, 
    "geteuid"               : { "id": 345, "threat": 4 }, 
    "geteuid32"             : { "id": 346, "threat": 4 }, 
    "getgid"                : { "id": 347, "threat": 4 }, 
    "getgid32"              : { "id": 348, "threat": 4 }, 
    "getgroups"             : { "id": 349, "threat": 4 }, 
    "getgroups32"           : { "id": 350, "threat": 4 }, 
    "getpgid"               : { "id": 351, "threat": 4 }, 
    "getpgrp"               : { "id": 352, "threat": 4 }, 
    "getpid"                : { "id": 353, "threat": 4 }, 
    "getppid"               : { "id": 354, "threat": 4 }, 
    "getrandom"             : { "id": 355, "threat": 4 }, 
    "getrusage"             : { "id": 356, "threat": 4 }, 
    "getsid"                : { "id": 357, "threat": 4 }, 
    "gettid"                : { "id": 358, "threat": 4 }, 
    "getuid"                : { "id": 359, "threat": 4 }, 
    "getuid32"              : { "id": 360, "threat": 4 },
    "sched_get_priority_max": { "id": 361, "threat": 4 }, 
    "sched_get_priority_min": { "id": 362, "threat": 4 }, 
    "sched_getaffinity"     : { "id": 363, "threat": 4 }, 
    "sched_getattr"         : { "id": 364, "threat": 4 },
    "sched_getparam"        : { "id": 365, "threat": 4 }, 
    "sched_getscheduler"    : { "id": 366, "threat": 4 }, 
    "sched_rr_get_interval" : { "id": 367, "threat": 4 }, 
    "sgetmask"              : { "id": 368, "threat": 4 }, 
    "ugetrlimit"            : { "id": 369, "threat": 4 },
    "pdflush"               : { "id": 370, "threat": 4 },
    "cacheflush"            : { "id": 371, "threat": 4 }, 
    "get_mempolicy"         : { "id": 372, "threat": 4 }, 
    "get_thread_area"       : { "id": 373, "threat": 4 },
    "clock_getres"          : { "id": 374, "threat": 4 }, 
    "clock_gettime"         : { "id": 375, "threat": 4 }, 
    "gettimeofday"          : { "id": 376, "threat": 4 }, 
    "time"                  : { "id": 377, "threat": 4 }, 
    "timer_getoverrun"      : { "id": 378, "threat": 4 }, 
    "timer_gettime"         : { "id": 379, "threat": 4 },
    "timerfd_gettime"       : { "id": 380, "threat": 4 }, 
    "times"                 : { "id": 381, "threat": 4 },
    "getpeername"           : { "id": 382, "threat": 4 }, 
    "getsockname"           : { "id": 383, "threat": 4 }, 
    "getsockopt"            : { "id": 384, "threat": 4 }, 
    "msgget"                : { "id": 385, "threat": 4 },
    "fsconfig"              : { "id": 386, "threat": 4 }, 
    "getpriority"           : { "id": 387, "threat": 4 }, 
    "oldolduname"           : { "id": 388, "threat": 4 }, 
    "olduname"              : { "id": 389, "threat": 4 }, 
    "shutdown"              : { "id": 390, "threat": 4 }, 
    "sysinfo"               : { "id": 391, "threat": 4 }, 
    "uname"                 : { "id": 392, "threat": 4 }, 
    "afs_syscall"           : { "id": 393, "threat": 4 }, 
    "break"                 : { "id": 394, "threat": 4 }, 
    "ftime"                 : { "id": 395, "threat": 4 }, 
    "getpmsg"               : { "id": 396, "threat": 4 }, 
    "gtty"                  : { "id": 397, "threat": 4 }, 
    "idle"                  : { "id": 398, "threat": 4 }, 
    "lock"                  : { "id": 399, "threat": 4 }, 
    "madvise1"              : { "id": 400, "threat": 4 }, 
    "mpx"                   : { "id": 401, "threat": 4 }, 
    "phys"                  : { "id": 402, "threat": 4 }, 
    "prof"                  : { "id": 403, "threat": 4 }, 
    "profil"                : { "id": 404, "threat": 4 },
    "putpmsg"               : { "id": 405, "threat": 4 }, 
    "security"              : { "id": 406, "threat": 4 }, 
    "stty"                  : { "id": 407, "threat": 4 }, 
    "tuxcall"               : { "id": 408, "threat": 4 }, 
    "ulimit"                : { "id": 409, "threat": 4 }, 
    "vserver"               : { "id": 410, "threat": 4 }, 
    "unimplemented"         : { "id": 411, "threat": 4 }, 
    "ftime"                 : { "id": 412, "threat": 4 }, 
    "ulimit"                : { "id": 413, "threat": 4 },
    "bdflush"               : { "id": 414, "threat": 4 }, 
    "futimesat"             : { "id": 415, "threat": 4 }, 
    "get_kernel_syms"       : { "id": 416, "threat": 4 }, 
    "query_module"          : { "id": 417, "threat": 4 }, 
    "remap_file_pages"      : { "id": 418, "threat": 4 }, 
    "xtensa"                : { "id": 419, "threat": 4 },
    "epoll_pwait"           : { "id": 420, "threat": 4 }, 
    "epoll_wait"            : { "id": 421, "threat": 4 }, 
    "fdatasync"             : { "id": 422, "threat": 4 }, 
    "fsync"                 : { "id": 423, "threat": 4 }, 
    "epoll_wait_old"        : { "id": 424, "threat": 4 },
    "oldumount"             : { "id": 425, "threat": 5 }, 
    "pwrite"                : { "id": 426, "threat": 5 }, 
    "pwrite64"              : { "id": 427, "threat": 5 }, 
    "s390_guarded_storage"  : { "id": 428, "threat": 5 }, 
    "spu_create"            : { "id": 429, "threat": 5 }, 
    "spu_run"               : { "id": 430, "threat": 5 },
    "arc_gettls"            : { "id": 431, "threat": 5 }, 
    "arc_settls"            : { "id": 432, "threat": 5 }, 
    "arc_usr_cmpxchg"       : { "id": 433, "threat": 5 }, 
    "atomic_barrier"        : { "id": 434, "threat": 5 }, 
    "atomic_cmpxchg_32"     : { "id": 435, "threat": 5 },
    "bfin_spinlock"         : { "id": 436, "threat": 5 }, 
    "breakpoint"            : { "id": 437, "threat": 5 }, 
    "execv"                 : { "id": 438, "threat": 5 }, 
    "old_getrlimit"         : { "id": 439, "threat": 5 }, 
    "perfctr"               : { "id": 440, "threat": 5 }, 
    "perfmonctl"            : { "id": 441, "threat": 5 },
    "s390_runtime_instr"    : { "id": 442, "threat": 5 }, 
    "sched_get_affinity"    : { "id": 443, "threat": 5 }, 
    "sched_set_affinity"    : { "id": 444, "threat": 5 }, 
    "setpgrp"               : { "id": 445, "threat": 5 }, 
    "switch_endian"         : { "id": 446, "threat": 5 },
    "s390_sthyi"            : { "id": 447, "threat": 5 },
    "dma_memcpy"            : { "id": 448, "threat": 5 }, 
    "getpagesize"           : { "id": 449, "threat": 5 }, 
    "memory_ordering"       : { "id": 450, "threat": 5 }, 
    "metag_get_tls"         : { "id": 451, "threat": 5 }, 
    "metag_set_fpu_flags"   : { "id": 452, "threat": 5 },
    "metag_set_tls"         : { "id": 453, "threat": 5 }, 
    "metag_setglobalbit"    : { "id": 454, "threat": 5 }, 
    "membarrier"            : { "id": 455, "threat": 5 }, 
    "memfd_create"          : { "id": 456, "threat": 5 }, 
    "migrate_pages"         : { "id": 457, "threat": 5 },
    "riscv_flush_icache"    : { "id": 458, "threat": 5 }, 
    "s390_pci_mmio_read"    : { "id": 459, "threat": 5 }, 
    "s390_pci_mmio_write"   : { "id": 460, "threat": 5 }, 
    "shmat"                 : { "id": 461, "threat": 5 }, 
    "shmctl"                : { "id": 462, "threat": 5 },
    "shmdt"                 : { "id": 463, "threat": 5 }, 
    "shmget"                : { "id": 464, "threat": 5 }, 
    "spill"                 : { "id": 465, "threat": 5 }, 
    "sram_alloc"            : { "id": 466, "threat": 5 }, 
    "sram_free"             : { "id": 467, "threat": 5 }, 
    "subpage_prot"          : { "id": 468, "threat": 5 },
    "old_adjtimex"          : { "id": 469, "threat": 5 },
    "getdomainname"         : { "id": 470, "threat": 5 }, 
    "gethostname"           : { "id": 471, "threat": 5 }, 
    "getxgid"               : { "id": 472, "threat": 5 }, 
    "getxpid"               : { "id": 473, "threat": 5 }, 
    "getxuid"               : { "id": 474, "threat": 5 }, 
    "rtas"                  : { "id": 475, "threat": 5 }, 
    "sethae"                : { "id": 476, "threat": 5 }, 
    "swapcontext"           : { "id": 477, "threat": 5 }, 
    "makecontext"           : { "id": 478, "threat": 5 }, 
    "sys_debug_setcontext"  : { "id": 479, "threat": 5 }, 
    "syscall"               : { "id": 480, "threat": 5 }, 
    "usr26"                 : { "id": 481, "threat": 5 }, 
    "usr32"                 : { "id": 482, "threat": 5 }, 
    "utrap_install"         : { "id": 483, "threat": 5 },
    "alloc_hugepages"       : { "id": 484, "threat": 5 }, 
    "free_hugepages"        : { "id": 485, "threat": 5 }, 
    "get_tls"               : { "id": 486, "threat": 5 }, 
    "getdtablesize"         : { "id": 487, "threat": 5 }, 
    "getunwind"             : { "id": 488, "threat": 5 }, 
    "set_tls"               : { "id": 489, "threat": 5 }, 
    "setup"                 : { "id": 490, "threat": 5 }, 
    "sysmips"               : { "id": 491, "threat": 5 },
    "_newselect"            : { "id": 492, "threat": 5 }, 
    "or1k_atomic"           : { "id": 493, "threat": 5 }, 
    "pciconfig_iobase"      : { "id": 494, "threat": 5 }, 
    "pciconfig_read"        : { "id": 495, "threat": 5 }, 
    "pciconfig_write"       : { "id": 496, "threat": 5 },

}
