
USER_GENDER_CHOICES = [('Female', 'Female'), ('Male', 'Male'),  ('Others', 'Others'),]

FILE_TYPE_MOBILE_BANNER = "MobileBanner"
FILE_TYPE_BANNER = "Banner"
FILE_TYPE_COVER_PROFILE_PIC = "CoverProfilePic"
FILE_TYPE_PROFILE_PIC = "ProfilePic"
FILE_TYPE_GALLERY = "Gallery"
FILE_TYPE_THUBNAIL = "Thumbnail"
FILE_TYPE_ADVERTISEMENT = "Adv"
FILE_TYPE_RESUME = "Resume"
FILE_TYPE_OTHERS = "Others"
FILE_TYPE_VIDEO = "Video"
FILE_TYPE_PICTURE = "Picture"
FILE_TYPE_360_PANO = "360_Pano"
FILE_TYPE_MARMOSET = "Marmoset_Viewer"
FILE_TYPES = [
    FILE_TYPE_MOBILE_BANNER,
    FILE_TYPE_BANNER,
    FILE_TYPE_COVER_PROFILE_PIC,
    FILE_TYPE_PROFILE_PIC,
    FILE_TYPE_GALLERY,
    FILE_TYPE_THUBNAIL,
    FILE_TYPE_ADVERTISEMENT,
    FILE_TYPE_RESUME,
    FILE_TYPE_OTHERS,
    FILE_TYPE_VIDEO,
    FILE_TYPE_PICTURE,
    FILE_TYPE_360_PANO,
    FILE_TYPE_MARMOSET
]
FILE_TYPE_CHOICES = [(a, a) for a in FILE_TYPES]