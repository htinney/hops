SOURCEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

JOB="/groups/dand"

SYMLINK_FOLDER="${JOB}/production/otls"

before=`pwd`
cd $SOURCEDIR
cd ../../hdas

for f in *.{hda,hdanc}
do
  if [ -f $f ]
  then
    echo "Copied" $f "to" "${SYMLINK_FOLDER}/${f}"
    cp $f "${SYMLINK_FOLDER}/${f}"
  fi
done

cd $before
